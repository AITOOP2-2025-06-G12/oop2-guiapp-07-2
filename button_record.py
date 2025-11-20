import ffmpeg

output_file = 'audio.wav'

class ButtonRecord:
    def button_record(self, duration: int = 10):
        try:
            (
                ffmpeg
                .input(':0', format='avfoundation', t=duration)
                .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
                .run(overwrite_output=True)
            )

        except ffmpeg.Error as e:
            # stderr が None の可能性があるので安全に処理
            err_msg = (e.stderr.decode() if e.stderr else "ffmpeg がエラーを返しました（stderr なし）")
            print("エラーが発生しました:", err_msg)

        except Exception as e:
            print("予期せぬエラー:", e)
