import asyncio, json
from playwright.async_api import async_playwright

URL = "https://makecode.microbit.org/#editor"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1280, "height": 860})
        await pg.goto(URL, timeout=120000, wait_until="domcontentloaded")
        for _ in range(60):
            ok = await pg.evaluate("() => (typeof Blockly!=='undefined' && Blockly.getMainWorkspace && !!Blockly.getMainWorkspace() && Blockly.getMainWorkspace().getAllBlocks().length>=0)")
            if ok: break
            await asyncio.sleep(2)
        await asyncio.sleep(3)
        # Dump ALL block type keys
        allkeys = await pg.evaluate("() => Object.keys(Blockly.Blocks || {}).filter(k=>/forever|on.?start|show.?string|start/i.test(k))")
        print("MATCHED_KEYS", json.dumps(allkeys))
        # also try via flyout: open Basic category and read rendered block types
        # The toolbox flyout blocks are <g> with attribute 'type' sometimes, or we read via Blockly.Toolbox
        tb = await pg.evaluate("""() => {
          try {
            const ws = Blockly.getMainWorkspace();
            const tb = ws.toolbox_;
            const cats = tb ? (tb.contents_ || []).map(c=>c.name_) : [];
            return {cats};
          } catch(e){ return {err:''+e}; }
        }""")
        print("TOOLBOX_CATS", json.dumps(tb))
        # Try querying the toolbox flyout rendered blocks types directly
        fb = await pg.evaluate("""() => {
          const els = Array.from(document.querySelectorAll('[data-shuffle] , .blocklyFlyout .blocklyDraggable'));
          const types = [];
          for (const e of els){
            const t = e.getAttribute && (e.getAttribute('type') || e.getAttribute('data-type'));
            if (t) types.push(t);
          }
          return types.slice(0,50);
        }""")
        print("FLYOUT_TYPES_SAMPLE", json.dumps(fb))
        await b.close()

asyncio.run(main())
