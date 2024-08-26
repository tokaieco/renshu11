import cv2
import streamlit as st
import time

def main():
    st.title("スマホカメラのライブ映像")
    
    # カメラを選択するためのオプション（通常、0が内蔵カメラ、1以降が外部カメラ）
    camera = st.selectbox("カメラを選択", [0, 1])
    
    # カメラを開く
    cap = cv2.VideoCapture(camera)
    
    if not cap.isOpened():
        st.error("カメラが見つかりませんでした")
        return

    # 初期化: 映像を表示するためのプレースホルダーを作成
    frame_placeholder = st.empty()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("カメラから映像が取得できませんでした")
            break
        
        # OpenCVのBGRをRGBに変換
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # 映像を更新
        frame_placeholder.image(frame)
        
        # 少しの遅延を追加
        time.sleep(0.03)  # 30ms = 約30fps

    cap.release()

if __name__ == "__main__":
    main()
