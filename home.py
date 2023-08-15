img = load_image('data:image/jpeg;base64,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')
      
st.image(img)
