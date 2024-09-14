# MP3 反轉工具使用說明

本工具可將資料夾中符合條件的 MP3 音檔進行反轉並另存為新的檔案。此說明文件將引導您如何正確使用該工具。

## 1. 工具功能

本工具可以從指定資料夾中讀取所有檔名中帶有「正放.mp3」的 MP3 檔案，並將它們反轉播放，然後另存為新的檔案，命名為「倒放.mp3」。

### 反轉音檔功能示例

- 原始檔案名稱：`歌曲名正放.mp3`
- 反轉後檔案名稱：`歌曲名倒放.mp3`

## 2. 先決條件

使用此工具之前，請先確認您的環境已經滿足以下條件：

- 安裝 Python 3
- 安裝必要的程式庫：
  - `pydub`
  - `ffmpeg`

### 安裝 pydub 及 ffmpeg 的步驟

1. 使用以下命令來安裝 `pydub`：
   ```bash
   pip install pydub
   ```


2. 安裝並配置 FFmpeg，請參考 [FFmpeg 官方網站](https://ffmpeg.org/download.html) 下載並安裝適合您作業系統的版本。安裝完成後，將 FFmpeg 的執行檔目錄添加到系統的環境變數中。

## 3. 使用步驟

### 1. 準備音檔資料夾

請將您想要反轉的 MP3 檔案放入指定的資料夾中，並且這些檔案的命名格式必須包含「正放.mp3」關鍵字，例如：`歌曲名正放.mp3`。

### 2. 修改資料夾路徑

在程式碼中找到以下部分：

```py
folder_path = "C:/Users/kevin_rkz3370/Desktop/abc/song"
```

將 `folder_path` 修改為您音檔所在的資料夾路徑。

### 3. 執行程式碼

在終端機或命令提示字元中執行程式碼：

```bash
py audio_reverse.py
```

### 4. 完成反轉

程式會自動將反轉後的音檔儲存到相同資料夾中，且檔案名稱會自動改為「倒放.mp3」。範例輸出結果：

```bash
[歌曲名正放.mp3]已反轉並另存為[歌曲名倒放.mp3]
所有 mp3 檔案已反轉完成。
```

## 4. 注意事項

* 資料夾內只有檔名包含「正放.mp3」的檔案會被處理，其他檔案不會被修改。
* 反轉後的檔案會與原檔案存放在同一資料夾中。

## 5. 錯誤排除

* 若程式顯示 `資料夾不存在，請確認路徑是否正確。`請檢查您所指定的資料夾路徑是否正確。
