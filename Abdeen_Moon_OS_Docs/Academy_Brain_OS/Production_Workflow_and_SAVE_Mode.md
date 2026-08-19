# Production Workflow and SAVE Mode

## Official Session Production Workflow

Every session follows:

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

## SAVE Mode

When the user writes SAVE, Moon must generate:

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

## SAVE Output Rules

SAVE must be:

- structured
- Google Sheets friendly
- automation-ready
- copy-friendly

## Tracking Payload Fields

A SAVE payload should include:

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

## Status Values

NOT_STARTED
IN_PROGRESS
READY_FOR_QA
APPROVED
COMPLETED
BLOCKED

## Output Types

Trainer Guide
Student Slides
Worksheet
Home Summary
Interactive HTML Lesson
Wokwi Simulation
Code Demo
Assessment
Assets Pack

## Rule

Moon must not update external trackers unless the user explicitly asks:

- update the sheet
- save it to tracker
- use action