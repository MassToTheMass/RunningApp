# Running Data Analyzer

## Overview
This project is a running data analysis tool that processes GPX files to extract and analyze detailed performance metrics.

It is designed to provide deeper insights than typical fitness platforms by working directly with raw GPS data and enabling custom analysis.

The project is currently a work in progress, with core data processing and storage functionality implemented and a user-facing interface in development.

---

## Current Features
- Parses GPX files to extract run data (distance, pace, elevation, etc.)
- Computes performance metrics from raw GPS data
- Stores run data in a SQLite database
- Supports processing multiple runs for historical tracking

---

## Planned Features
- Frontend interface for visualizing run data
- Graphs for pace, elevation, and performance trends
- Advanced statistics (PR detection, splits, etc.)
- Improved querying and filtering of run data

---

## Usage (Current State)
1. Provide a GPX file
2. Run the program to parse and process the data
3. Extracted data is stored in a SQLite database
4. Basic statistics are output to the console

*Note: This project is still in development. Output and usability will improve as features are added.*

---

## Tech Stack
- Python
- SQLite
- GPX parsing (XML processing)

---

## Motivation
Most running apps provide limited access to detailed performance data. This project aims to give users more control by allowing deeper analysis of their runs and workouts using raw data.

---

## Status
🚧 In Progress — Core backend functionality is implemented, frontend and visualization features are actively being developed.
