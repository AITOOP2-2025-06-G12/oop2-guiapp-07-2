import os

class ButtonSave:
    """
    文字起こしされた文字列を保存するクラス
    """

    def outputTextFile(self, text: str):
        """
        text を audio.txt として保存（重複時は audio2.txt, audio3.txt ...）
        """

        filename = 'audio.txt'
        name, ext = os.path.splitext(filename)

        filename_to_use = filename
        counter = 2

        while os.path.exists(filename_to_use):
            filename_to_use = f"{name}{counter}{ext}"
            counter += 1

        try:
            with open(filename_to_use, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"保存完了: {filename_to_use}")
        except Exception as e:
            print(f"ファイル書き込み中にエラーが発生しました: {e}")
