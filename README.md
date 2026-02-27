# AI Hiring Assistant

This repository contains two complementary desktop applications that together form an AI-powered recruitment assistant.

- **`interviewee_side`** – self-contained PyQt6 GUI used by a candidate to register, align their face, record interview answers, and complete a personality assessment. All data is stored locally in a shared `user_data` directory.
- **`interviewer_side/AIHiringAssistant`** – analysis and monitoring tools for the recruiter, including thermal/visual camera interfaces, ML models for personality prediction, and a separate PyQt6 UI for browsing sessions and viewing results.

---

## Common Requirements

Both sides are written in Python (3.9+) and rely on the following packages:

```sh
pip install -r interviewee_side/requirements.txt
pip install -r interviewer_side/AIHiringAssistant/requirements.txt
```

You will also need a working webcam and, optionally, MediaPipe for improved face detection.

> On Windows you may need to install the `opencv-python` package with ffmpeg support if you require MP4 video writing.

## Interviewee Side

### Overview
The `interviewee_side` app guides candidates through:
1. **Landing page** with animated UI.
2. **Registration** form (name, email, etc.).
3. **Face alignment** using the webcam; ensures the candidate is looking at the camera.
4. **Interview** phase where answers to questions are recorded as MP4 files.
5. **OCEAN personality assessment** questionnaire.
6. **Results** summary showing their registration data, video path and computed trait averages.

Key modules:
- `src/app.py` – main controller managing navigation and session lifecycle.
- `src/data_manager.py` – file I/O for sessions, registration, recordings and summaries.
- `src/camera_handler.py` – threaded webcam manager with face/pose detection and video recording.
- `src/pages/` – PyQt6 widgets for each page, richly styled.

All session data is written under `../interviewer_side/AIHiringAssistant/user_data/session_<timestamp>/`.

### Running
```sh
python interviewee_side/main.py
```

## Interviewer Side (`AIHiringAssistant`)

### Overview
This directory contains tools used by the recruiter/analyst:

- **Core modules** (`core/`): camera management (visual/thermal), face alignment logic, landmark detection, GAN validator, session handling, thermal processing, and data logging.
- **ML pipeline** (`ml/`): dataset builder, feature extraction, model training (`ocean_mlp_model.pkl`), and prediction helper functions.
- **UI** (`ui/`): PyQt6 pages for home, session selection, alignment tools, and ML result display.
- **Utilities/tests**: simple scripts to verify imports and ingest video.

The ML code expects CSV logs produced by `core/data_logger.py`; predictions can be executed via `ml/predict.py`.

### Running
```sh
python interviewer_side/AIHiringAssistant/main.py
```

This will launch a PyQt6 window allowing you to browse recorded sessions, perform alignment calibration, and run the personality model on a selected session.

### Data
Recorded sessions and CSV logs live in `interviewer_side/AIHiringAssistant/data/`:
- `output_logs/` – per-frame landmarks and temperature recordings.
- `videos/` – raw video feeds if captured manually.
- `user_data/` – replicated from the interviewee side (registration, assessment, summaries).

## Development Notes

- **Architecture**: Both applications are structured around PyQt6's `QStackedWidget` for page navigation.
- **Face detection**: Interviewee side prefers MediaPipe (optional) and falls back to Haar cascades. Interviewer side uses custom landmark detectors and alignment logic.
- **Session IDs**: Format `session_YYYYMMDD_HHMMSS` based on timestamp.
- **Styling**: The interviewee UI uses a `GLOBAL_STYLESHEET` in `src/styles.py` for a cohesive look.

## Extending

- Add new interview questions by editing `assets/interview_questions.json`.
- Update ML feature extraction in `interviewer_side/AIHiringAssistant/ml/features.py` and retrain using `build_dataset.py`.
- Use `verify_ui_import.py` or other test scripts to ensure dependencies are met.

---

**License**: [Add as appropriate]

**Author**: [Your Name] – originally developed by the AARYAN GUI team.
