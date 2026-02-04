## UKZN Smart Timetable Generator

A personal software project that generates a unified weekly timetable for UKZN students by extracting and normalising scheduling information from module timetable PDFs.

The system accepts individual module timetables and produces a single, structured PDF timetable containing session times, venues, and module details.

---

## Project Overview

UKZN module timetables are typically distributed as separate, semi-structured PDF documents. When students register for multiple modules, they must manually interpret these documents and combine the information into a usable weekly schedule.

This project automates that process by:
- Extracting timetable data from module PDFs
- Normalising session information
- Detecting scheduling conflicts
- Generating a consolidated PDF timetable

---

## Development Approach

The project is implemented in two phases.

### Phase 1: Python Prototype

The first phase focuses on:
- PDF text extraction
- Parsing and normalisation of timetable data
- Validating assumptions about UKZN timetable formats

Python is used to rapidly develop and test the parsing logic before committing to a full system implementation.

### Phase 2: Java System

The second phase reimplements the validated logic as a structured Java application with:
- A clear domain model
- Layered architecture
- Unit testing
- Maintainable and extensible code

---

## Input
 - PDF module timetables obtained from the UKZN CELCAT system
 - One PDF per module

## Output
 - A single PDF timetable displaying:
 - Day of the week
 - Start and end time
 - Module code
 - Module name
 - Session type (Lecture, Practical, Tutorial)
 - Venue
Scheduling conflicts are flagged in the output.

## Testing
 - Unit tests for time parsing
 - Unit tests for conflict detection
 - Manual verification using real UKZN timetable PDFs

## Technologies
### Phase 1
 - Python 3
 - PDF text extraction libraries
 - Regex-based parsing
 - PDF generation libraries

### Phase 2
 - Java 17+
 - Apache PDFBox
 - Maven
 - JUnit 5
 - Java Time API
