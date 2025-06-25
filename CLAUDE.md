# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a human-computer interaction research project studying On-Screen Display (OSD) navigation using different hardware input methods (mouse wheel, D-pad, joystick). The study compares hardware types and UI designs through reaction time (RT) and accuracy (ACC) experiments.

## Core Architecture

### Experimental Framework
- **PsychoPy-based**: All experiments use PsychoPy for visual stimuli and hardware interface
- **Hardware Abstraction**: `ResponseTrigger.py` provides unified input handling across different devices
- **Material System**: `OSD_Material.py` and `Solarized.py` define UI elements and color schemes
- **Data Collection**: Each experiment generates timestamped data files for analysis

### Key Modules
- `ResponseTrigger.py`: Handles input from mouse wheel, D-pad, and joystick
- `OSD_Material.py`: Defines UI layout positions and pseudo-random sequences
- `Solarized.py`: Contains color palette definitions
- `StiGenerator.py`: Generates experimental stimuli

### Experiment Types
1. **OSD Navigation** (`OSD_simulate.py`): Multi-layer menu navigation
2. **Reaction Time** (`RT_focus.py`): Simple directional response tasks  
3. **Accuracy** (`ACC_focus.py`): Precision-focused tasks
4. **Button-to-Screen** (`BTS_simulation.py`): Hardware-specific navigation

## Hardware Configuration

### Monitor Setup
- Default: 2560x1440 ProArt27 monitor
- Viewing distance: 60cm
- Monitor width: 60cm
- Supports dual-screen setup (main screen 0, external screen 1)

### Input Devices
- Mouse wheel with click detection
- D-pad/joystick via PsychoPy joystick backend
- Subject assignment alternates hardware order (odd/even ID)

## Running Experiments

### Python Experiments
```bash
cd expRT/
python OSD_simulate.py    # OSD navigation experiment
python RT_focus.py        # Reaction time experiment  
python ACC_focus.py       # Accuracy experiment
python BTS_simulation.py  # Button-to-screen experiment
```

### Practice Sessions
```bash
python OSD_practice.py    # OSD practice trials
python RT_practice.py     # RT practice trials
python ACC_practice.py    # ACC practice trials
```

## Data Analysis

### R Analysis Scripts
```bash
# Navigate to DataAnalysis/ directory
Rscript OSD-RECAL.R      # Main OSD analysis
Rscript ReactionTime.R   # RT analysis
Rscript AccuracyRate.R   # Accuracy analysis
Rscript countAnalysis.R  # Count-based analysis
```

### Python Data Processing
```bash
python MergeData.py           # Merge multiple data files
python MergeAccidentTrigger.py # Process accident triggers
python MergeDeliberate.py     # Process deliberate actions
```

## Dependencies

- PsychoPy (visual, event, core, monitors, hardware)
- NumPy
- R with tidyverse, ggpubr, rstatix, dplyr, nlme, multcomp, ggplot2

## Data Structure

Experiments generate tab-separated data files with columns:
- ID, Device, Direction, Answer, Step, Time, RT, Trial info
- Hardware-specific response codes
- Timestamp and accuracy triggers

## File Organization

- `expRT/`: Main experiment scripts and assets
- `DataAnalysis/`: R scripts and processed data files
- `WheelOSDtest/`: Legacy/prototype code
- `expRT/*_ImgFolder/`: Image assets for each experiment type