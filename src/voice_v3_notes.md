# Lucky v0.3.0 — Voice edition

The original voice prototype uses whisper.cpp for speech-to-text and Windows System.Speech for text-to-speech. Keep your existing `whisper/Release/whisper-cli.exe` and model file outside Git (they are ignored).

This package preserves the v0.1 CLI and provides the v0.2 web-chat API. The voice implementation should be merged from your existing local `src/voice.py` / saved voice-enabled `main.py` backup when promoting v0.3. Those original files were not present in the supplied v0.1 ZIP, so this note deliberately does not pretend to reproduce their exact implementation.
