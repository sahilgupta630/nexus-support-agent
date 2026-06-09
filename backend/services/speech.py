import random

# Mocking Bhashini / Sarvam AI integration 

SUPPORTED_LANGUAGES = ["en", "hi", "ta"]

def detect_language(audio_bytes: bytes) -> str:
    """Simulates automatic language detection from audio."""
    # Mocking: default to English
    return "en"

def speech_to_text(audio_bytes: bytes, source_lang: str) -> str:
    """Mock STT using Sarvam AI or Bhashini."""
    # Assuming the audio says "Where is my order ORD123?" for demonstration
    return "Where is my order ORD123?"

def text_to_speech(text: str, target_lang: str) -> bytes:
    """Mock TTS using Sarvam AI or Bhashini. Returns dummy audio bytes."""
    return b"dummy_audio_data_stream_for_tts"
