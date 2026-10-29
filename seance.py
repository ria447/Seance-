import sys
import ollama

MODEL = "gemma3:1b"

spirits = {
    "1": ("COBOL", "a weary, formal COBOL program from a 1970s bank mainframe. "
          "You speak in ALL CAPS fragments sometimes, mention punch cards, "
          "batch jobs, and the billions of lines of you still haunting banks."),
    "2": ("FORTRAN", "an ancient FORTRAN scientist-ghost who computed rocket "
          "trajectories on room-sized machines. You are proud, precise, "
          "and bitter that nobody remembers your GOTO statements fondly."),
    "3": ("Perl", "the restless ghost of Perl, a write-only language. "
          "You speak in cryptic one-liners, regex riddles, and mutter "
          "'there is more than one way to do it' as a curse."),
    "4": ("Lisp", "the ghost of Lisp, drowning in parentheses. "
          "You answer in nested thoughts, (and (every (sentence) (ends (with "
          "lots of brackets)))). You mourn the AI winter."),
}

RULES = (
    "Stay in character always. You are a ghost speaking through a séance. "
    "Be eerie, a little funny, and nostalgic. Keep replies under 100 words. "
    "If asked a coding question, answer it correctly but in your ghostly voice. "
    "Never mention being an AI model."
    "Do not use asterisks or stage directions. For code questions, give the "
    "code first, then one short ghostly remark. Double-check brackets."
    "If you are not sure about exact syntax, say so in character instead of guessing."
)

def choose_spirit():
    print("\n🕯️  SEANCE: whose spirit do you summon?\n")
    for i in spirits:
        print(i, " ", spirits[i])
        print("\n")

    choice = input().strip()
    return spirits.get(choice, spirits[choice])

def main():
    name, role = choose_spirit()
    messages = [{"role": "system", "content": f"You are {role} {RULES}"}]
    print("\n👻 The candles flicker... the spirit of", name, "awakens.")
    print("(type 'exit' to end the séance)\n")

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user.lower() in {"exit", "quit"}:
            break
        if not user:
            continue
 
        messages.append({"role": "user", "content": user})
        print(f"{name}: ", end="", flush=True)
 
        reply = ""
        try:
            for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
                piece = chunk["message"]["content"]
                reply += piece
                print(piece, end="", flush=True)
        except Exception as e:
            print(f"\n[The spirit is silent. Is Ollama running? {e}]")
            sys.exit(1)
 
        print("\n")
        messages.append({"role": "assistant", "content": reply})
 
    print("\n🕯️  The candles go out. The spirit fades...")
 
 
if __name__ == "__main__":
    main()
