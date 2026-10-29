# 🕯️Seance-

Built for the Hacktoberfest Open-Source AI Challenge, Week 4: Ghost in the Machine.

SEANCE is a terminal chatbot where you summon the spirit of a *dead (or dying) programming language* and talk to it. You can choose any one of COBOL, FORTRAN, Perl or Lisp, and the ghost answers in its own voice. COBOL mourns punch cards and batch jobs, FORTRAN is bitter that nobody remembers it fondly, Perl speaks in cryptic one-liners, and Lisp drowns in parentheses.

| # | Spirit | Personality |
|---|--------|-------------|
| 1 | COBOL | Weary bank-mainframe veteran, haunted by punch cards and batch jobs |
| 2 | FORTRAN | Proud rocket-trajectory scientist, bitter that nobody remembers it |
| 3 | Perl | Cryptic one-liners and regex riddles |
| 4 | Lisp | Drowning in parentheses, mourning the AI winter |

They will still answer real coding questions, just in character.

## Why open-source AI?

- **Works with Wi-Fi off.** Everything runs locally; no API, no cloud.
- **Free to run.** No API key, no billing, no limits.
- **Private.** Nothing you type leaves your machine.
- **Swappable.** Change one line (`MODEL = "gemma3:1b"`) to try another open model.

## Built with

- [Gemma 3 1B](https://ollama.com/library/gemma3) (open-weight model by Google)
- [Ollama](https://ollama.com) for local inference
- Python + the `ollama` library (streaming responses)

## Setup

1. Install Ollama from https://ollama.com
2. Download the model:
   ```
   ollama pull gemma3:1b
   ```
3. Install the Python library:
   ```
   pip install ollama
   ```
4. Run:
   ```
   python seance.py
   ```

Pick a spirit by typing its number, chat, and type `exit` to end the séance.

## Add your own spirit

Each ghost is just a persona prompt in the `SPIRITS` dictionary in `seance.py`:

```python
"5": ("Flash", "the ghost of Adobe Flash, mourning the browser games that died in 2020..."),
```

No retraining, no new model download.

## Known limitations

The 1B model nails the personas but **not exact syntax**. The Lisp ghost once added an extra closing parenthesis, and the FORTRAN ghost repeatedly wrote BASIC-style pseudo-code instead of real FORTRAN. Treat SEANCE as entertainment, not a coding assistant. For better code accuracy, swap in a larger open model (e.g. `gemma3:4b`).

## License

MIT
