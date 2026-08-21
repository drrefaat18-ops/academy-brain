import asyncio, json
from playwright.async_api import async_playwright

URL = "https://makecode.microbit.org/#editor"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1280, "height": 860})
        await pg.goto(URL, timeout=120000, wait_until="domcontentloaded")
        # wait for Blockly main workspace
        for _ in range(60):
            ok = await pg.evaluate("() => (typeof Blockly!=='undefined' && Blockly.getMainWorkspace && !!Blockly.getMainWorkspace())")
            if ok:
                break
            await asyncio.sleep(2)
        # ensure blocks mode
        info = await pg.evaluate("""() => {
          const out = {};
          try { out.pxt = typeof pxt; } catch(e){ out.pxt='ERR '+e; }
          try { out.blocksApi = (pxt && pxt.blocks) ? Object.getOwnPropertyNames(pxt.blocks).slice(0,40) : null; } catch(e){ out.blocksApi='ERR '+e; }
          // collect block type names that look relevant
          const types = Object.keys(Blockly.Blocks || {});
          out.forever = types.filter(t=>/forever/i.test(t));
          out.onstart = types.filter(t=>/on.?start|onstart/i.test(t));
          out.showstring = types.filter(t=>/show.?string/i.test(t));
          out.basicCat = (pxt && pxt.appTarget && pxt.appTarget.bundledpkgs) ? Object.keys(pxt.appTarget.bundledpkgs).slice(0,30) : null;
          return out;
        }""")
        print("DISCOVERY", json.dumps(info, indent=1, default=str))
        # dump a sample show-string / forever block's input+field names if present
        detail = await pg.evaluate("""() => {
          const types = Object.keys(Blockly.Blocks || {});
          const res = {};
          for (const t of types) {
            if (/forever|on.?start|show.?string/i.test(t)) {
              const def = Blockly.Blocks[t];
              res[t] = {
                init_src: (def && def.init && def.init.toString) ? def.init.toString().slice(0,400) : 'no-init'
              };
            }
          }
          return res;
        }""")
        print("BLOCKDEFS")
        for k,v in detail.items():
            print("TYPE", k)
            print(v['init_src'])
        await b.close()

asyncio.run(main())
