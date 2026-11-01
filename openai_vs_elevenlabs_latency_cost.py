#!/usr/bin/env python3
"""
OpenAI TTS vs ElevenLabs API Latency & Million-Character Cost Calculator 2026.
"""
import argparse

def calculate(million_chars, turbo):
    openai_cost = million_chars * 15.0  # tts-1 standard $15 / 1M chars
    openai_hd = million_chars * 30.0    # tts-1-hd $30 / 1M chars

    # ElevenLabs API Scale rate
    eleven_rate = 100.0 if turbo else 180.0
    eleven_cost = million_chars * eleven_rate

    print("=" * 60)
    print("API Voice Synthesis: OpenAI TTS vs ElevenLabs API")
    print("=" * 60)
    print(f"Monthly Traffic:         {million_chars:.2f} Million Characters")
    print(f"OpenAI TTS-1 Standard:   ${openai_cost:.2f}/mo (Latency ~250ms)")
    print(f"OpenAI TTS-1-HD:         ${openai_hd:.2f}/mo (Latency ~400ms)")
    print(f"ElevenLabs Turbo API:    ${eleven_cost:.2f}/mo (Latency ~150ms)")
    print(f"Premium for Realism:     ${(eleven_cost - openai_cost):.2f}/mo")
    print("=" * 60)
    return openai_cost, eleven_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenAI vs ElevenLabs API Calculator")
    parser.add_argument("--million-chars", type=float, default=2.5)
    parser.add_argument("--turbo", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.million_chars, args.turbo)
