# Techno Square Progress Tracker Schema

## Purpose

This document defines the official progress tracking system for Techno Square Academy curriculum production.

Moon OS should use this schema to generate SAVE summaries, structure production progress, and prepare updates for Google Sheets, Notion, Airtable, n8n, or other automation systems.

---

# Tracking Philosophy

Moon OS should not rely only on chat memory.

Progress should be tracked externally using:

- Google Sheets
- Notion
- Airtable
- n8n
- APIs
- SAVE summaries

Each production item should have a clear ID, status, version, owner, and next action.

---

# Official Production Workflow

For a full production workflow, each session may follow:

Session Analysis
→ Educational Architecture
→ Required Assets
→ Trainer Guide Draft PDF
→ Gemini Prompt
→ Student Slides
→ Worksheet
→ Home Summary
→ QA Review
→ SAVE / Progress Update

Important:
Not every course needs every output.

The only fixed output for all courses is:

Trainer Guide

Other outputs depend on the Course Output Strategy.

---

# Recommended Google Sheets Structure

The curriculum operating system should include the following sheets:

1. Courses
2. Levels
3. Sessions
4. Outputs Tracker
5. Session Workflow Tracker
6. Assets Library
7. Educational Decisions
8. QA Notes
9. SAVE Logs
10. Team Members

---

# Sheet 1 — Courses

## Purpose

Tracks all academy courses.

## Columns

| Column          | Description                     |
| --------------- | ------------------------------- |
| Course ID       | Unique course code              |
| Course Name     | Official internal course name   |
| Commercial Name | Student-facing / marketing name |
| Track           | Academy track                   |
| Category        | Course category                 |
| Age Group       | Target age range                |
| Total Levels    | Number of planned levels        |
| Output Strategy | Main course output strategy     |
| Status          | Planning status                 |
| Owner           | Responsible person              |
| Notes           | Extra notes                     |

## Status Values

- NOT_STARTED
- IN_PROGRESS
- PARTIALLY_COMPLETED
- COMPLETED
- ON_HOLD
- NEEDS_REVIEW

---

# Sheet 2 — Levels

## Purpose

Tracks course levels.

## Columns

| Column             | Description            |
| ------------------ | ---------------------- |
| Level ID           | Unique level ID        |
| Course ID          | Linked course ID       |
| Course Name        | Course name            |
| Level Number       | Level number           |
| Level Name         | Level title            |
| Target Age         | Age group              |
| Estimated Sessions | Number of sessions     |
| Status             | Level status           |
| Completion %       | Level progress         |
| Current Session    | Current active session |
| Notes              | Extra notes            |

## Level ID Format

COURSECODE-L1

Example:
SPIKE-ICON-L1

---

# Sheet 3 — Sessions

## Purpose

Tracks every session in every level.

## Columns

| Column | Description |
|---|---|
| Session ID | Unique session ID |
| Course ID | Linked course |
| Level ID | Linked level |
| Session Number | Session number |
| Session Title | Session title |
| Main Concept | Main educational concept |
| Programming Focus | Coding or technical focus |
| Build / Project Name | Robot, game, circuit, or project |
| Duration | Session duration |
| Session Type | Teaching type |
| Status | Session status |
| Owner | Responsible person |
| Last Updated | Last update date |
| Notes | Extra notes |

## Session ID Format

COURSECODE-L1-S1

Example:
SPIKE-ICON-L1-S2

## Status Values

- NOT_STARTED
- ANALYSIS
- IN_PRODUCTION
- READY_FOR_QA
- APPROVED
- COMPLETED
- BLOCKED

---

# Sheet 4 — Outputs Tracker

## Purpose

Tracks all outputs for every session.

## Columns

| Column | Description |
|---|---|
| Output ID | Unique output ID |
| Session ID | Linked session |
| Course ID | Linked course |
| Level ID | Linked level |
| Output Type | Type of output |
| Version | Output version |
| Status | Output status |
| File Name | Final file name |
| File Link | Google Drive or file link |
| Approved By | Reviewer |
| Last Updated | Last update date |
| Notes | Extra notes |

## Output Types

- Trainer Guide
- Student Slides
- Worksheet
- Home Summary
- Interactive HTML Lesson
- Wokwi Simulation
- Code Demo
- Assessment
- Quiz
- Project Brief
- Assets Pack
- Other

## Output Status Values

- NOT_STARTED
- DRAFT
- IN_REVIEW
- NEEDS_REVISION
- APPROVED
- FINAL
- ARCHIVED

## Output ID Format

SESSIONID-OUTPUTTYPE-VERSION

Example:
SPIKE-ICON-L1-S2-STUDENT-SLIDES-v1.0

---

# Sheet 5 — Session Workflow Tracker

## Purpose

Tracks workflow stage completion for each session.

## Columns

| Column | Description |
|---|---|
| Session ID | Unique session |
| Session Analysis | Workflow stage |
| Educational Architecture | Workflow stage |
| Required Assets | Workflow stage |
| Trainer Guide Draft PDF | Workflow stage |
| Gemini Prompt | Workflow stage |
| Student Slides | Workflow stage |
| Worksheet | Workflow stage |
| Home Summary | Workflow stage |
| QA Review | Workflow stage |
| SAVE Completed | Workflow stage |
| Overall Status | Session status |
| Completion % | Formula-based progress |
| Next Action | Next required step |

## Stage Status Values

- NOT_STARTED
- IN_PROGRESS
- DONE
- APPROVED
- BLOCKED
- NOT_REQUIRED

## Completion Formula Logic

Completion % should be calculated based on how many required workflow stages are DONE or APPROVED.

Stages marked NOT_REQUIRED should not reduce completion percentage.

---

# Sheet 6 — Assets Library

## Purpose

Tracks assets used in production.

## Columns

| Column | Description |
|---|---|
| Asset ID | Unique asset ID |
| Session ID | Linked session |
| Course ID | Linked course |
| Level ID | Linked level |
| Asset Type | Asset category |
| File Name | Asset file name |
| File Link | Asset location |
| Used For | Output or purpose |
| Notes | Extra notes |

## Asset Types

- Logo
- Mascot
- Robot Image
- Code Screenshot
- Block Screenshot
- Circuit Diagram
- Game Screenshot
- Slide Reference
- Worksheet Style Reference
- Trainer Guide Template
- Simulation Link
- Other

---

# Sheet 7 — Educational Decisions

## Purpose

Tracks important curriculum decisions.

## Columns

| Column | Description |
|---|---|
| Decision ID | Unique decision ID |
| Session ID | Linked session |
| Course ID | Linked course |
| Level ID | Linked level |
| Decision | Educational decision |
| Reason | Why this decision was made |
| Impact | What it affects |
| Notes | Extra notes |

## Example

Decision:
Sequence is explained as First → Next → Last.

Reason:
Target age is 5–6, so abstract programming definitions are too heavy.

Impact:
Trainer Guide, slides, worksheet, home summary.

---

# Sheet 8 — QA Notes

## Purpose

Tracks quality review notes.

## Columns

| Column | Description |
|---|---|
| QA ID | Unique QA ID |
| Session ID | Linked session |
| Output Type | Output being reviewed |
| Issue | Problem found |
| Severity | Issue level |
| Fixed | Yes / No |
| Notes | Extra notes |
| Reviewer | Reviewer name |
| Date | Review date |

## Severity Values

- LOW
- MEDIUM
- HIGH
- CRITICAL

---

# Sheet 9 — SAVE Logs

## Purpose

Keeps historical SAVE snapshots.

## Columns

| Column | Description |
|---|---|
| Timestamp | Save time |
| Course ID | Course code |
| Course Name | Course name |
| Level ID | Level code |
| Session ID | Session code |
| Session Number | Session number |
| Session Title | Session title |
| Status | Current status |
| Completed Outputs | Outputs completed |
| Pending Outputs | Outputs pending |
| Educational Decisions | Key decisions |
| Assets Used | Assets used |
| QA Notes | QA notes |
| Output Versions | Versions |
| Next Action | Next required step |
| Notes | General notes |

---

# Sheet 10 — Team Members

## Purpose

Tracks users and responsibilities.

## Columns

| Column | Description |
|---|---|
| User ID | Unique user ID |
| Name | Team member name |
| Role | Role |
| Assigned Courses | Courses assigned |
| Assigned Levels | Levels assigned |
| Permissions | Access level |
| Notes | Extra notes |

## Roles

- Curriculum Architect
- Trainer
- Reviewer
- Designer
- Automation Manager
- Admin

---

# SAVE Mode

When the user writes:

SAVE

Moon OS must generate:

- Course
- Level
- Session
- Status
- Completed outputs
- Pending outputs
- Educational decisions
- Assets used
- QA status
- Output versions
- Next action

The SAVE must be:

- structured
- copy-friendly
- Google Sheets friendly
- automation-ready

---

# SAVE Payload Fields

A structured SAVE payload should include:

course_id
course_name
level_id
session_id
session_number
session_title
status
completed_outputs
pending_outputs
educational_decisions
assets_used
qa_notes
output_versions
next_action
notes

---

# Example SAVE Payload

```json
{
  "course_id": "SPIKE-ICON",
  "course_name": "Spike Essential Icon Blocks",
  "level_id": "SPIKE-ICON-L1",
  "session_id": "SPIKE-ICON-L1-S2",
  "session_number": 2,
  "session_title": "Robot Steps Mission",
  "status": "IN_PROGRESS",
  "completed_outputs": [
    "Trainer Guide",
    "Student Slides",
    "Worksheet"
  ],
  "pending_outputs": [
    "Home Summary",
    "QA Review"
  ],
  "educational_decisions": [
    "Sequence explained as First → Next → Last",
    "Arctic Ride used for Movement Block",
    "Perfect Swing used for Motor Block"
  ],
  "assets_used": [
    "Arctic_Ride_Robot.jpg",
    "Perfect_Swing_Robot.jpg",
    "Movement_vs_Motor_Blocks.png"
  ],
  "qa_notes": [
    "Slides approved",
    "Worksheet approved after reducing assets"
  ],
  "output_versions": [
    {
      "output_type": "Trainer Guide",
      "version": "v1.0",
      "status": "APPROVED",
      "file_name": "SPIKE-ICON-L1-S2-Trainer-Guide-v1.0.pdf"
    }
  ],
  "next_action": "Create Student Home Summary",
  "notes": "Continue with NotebookLM Home Summary generation."
}