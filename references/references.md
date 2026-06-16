# References & Analytical Decisions

## Project Cycle 4 — Sleep Duration and Feelings of Sadness or Hopelessness
** 113370219 謝紫旋**

---

## 1. 資料來源 | Data Source

**Dataset:** Youth Risk Behavior Surveillance System (YRBS) 2007

- **主辦單位:** Centers for Disease Control and Prevention (CDC)
- **原始檔案:** `YRBS_2007.csv`（共 14,041 筆，103 個變數）
- **官方網站:** https://www.cdc.gov/yrbs
- **官方報告:** CDC. (2008). *Youth Risk Behavior Surveillance — United States, 2007.* MMWR Surveillance Summaries, 57(SS-4). https://www.cdc.gov/mmwr/preview/mmwrhtml/ss5704a1.htm

---

## 2. 變數編碼 | Variable Coding

### Predictor Variable — `Sleep`
根據 YRBS 2007 官方問卷，代表受訪學生在學校日（School night）的平均睡眠時數。在本專題中將其視為代表睡眠時間長短的連續分數（Continuous Score）。

---

### Response Variable — `SadOrHopeless`
根據 YRBS 2007 官方問卷，題目為問及學生過去 12 個月內是否曾連續兩週或更長時間感到極度悲傷或絕望（Felt sad or hopeless）。
原始問卷中包含多種分類編碼，本專題對其進行二分法重編碼：

| 原始編碼 | 原始定義 | 本專題標籤 | 數值定義 |
|----------|------|-----------|:---:|
| 1 | Yes（感到悲傷或絕望） | `Yes` | **1** |
| 2 | No（未感到悲傷或絕望） | `No` | **0** |

---

## 3. 資料清理與排除條件 | Data Population & Exclusion

- **目標變數:** `Sleep` 與 `SadOrHopeless`
- **最終有效樣本數:** n = 12,106
- **排除條件:** 性別、睡眠時數或憂鬱情緒欄位任一為缺失值（NaN）者予以刪除。若 `SadOrHopeless` 包含原始問卷大於 1 的編碼，將自動對應轉換。

處理流程（參考 `06_sleep_sad_interpretation.ipynb`）：
```python
df = pd.read_csv(target_path)
if df['SadOrHopeless'].max() > 1:
    df['SadOrHopeless'] = df['SadOrHopeless'].map({1: 1, 2: 0})
df = df.dropna(subset=['Sleep', 'SadOrHopeless'])
