# 音声録音文字起こしアプリ

このアプリは **録音 → 文字起こし → 保存** の順に操作できる PySide6 GUI アプリケーションです。

---

## 動作環境

- Python 3.13
- PySide6
- mlx_whisper
- ffmpeg（macOS の場合は avfoundation 対応）
- 必要な Python モジュールは以下のコマンドでインストールしてください:

```bash
pip install PySide6 mlx_whisper

## 実行方法

1. リポジトリをクローンまたはダウンロードします。

```bash
git clone <リポジトリURL>
cd oop2-guiapp-07

2. Main.pyを実行する

## 使い方

1. **録音ボタン** を押す  
   - デフォルトで 10 秒間録音し、`audio.wav` に保存されます。

2. **文字起こしボタン** を押す  
   - 録音した音声を読み込み、文字起こしします。  
   - 文字起こし結果はコンソールにも表示されます。

3. **保存ボタン** を押す  
   - 文字起こし結果を `audio.txt` として保存します。  
   - すでに同名ファイルがある場合は `audio2.txt`, `audio3.txt` … と連番で保存されます。

