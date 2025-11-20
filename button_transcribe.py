import mlx_whisper

class ButtonTranscribe:
    """音声ファイルを指定して文字起こしをするクラス。
    Returns:
        result: 文字起こしの結果を含む関数。
    """

    def transcribe_audio(self):

        audio_file_path = 'audio.wav'

        # whisper-base-mlx を使って文字起こし
        result = mlx_whisper.transcribe(
            audio_file_path,
            path_or_hf_repo="./whisper-base-mlx"
        )

        print(result["text"])
        return result["text"]
