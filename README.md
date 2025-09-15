# Chatbot API

Bu proje, ... için geliştirilmiş bir Python tabanlı chatbot API'sidir.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi klonlayın:**
    ```bash
    git clone https://github.com/kemoagaben/chatbot_api.git
    cd chatbot_api
    ```

2.  **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı başlatın:**
    ```bash
    python main.py
    ```

API `http://localhost:8000` adresinde çalışacaktır.

## Docker

Projeyi Docker ile çalıştırmak için:

```bash
docker build -t chatbot-api .
docker run -p 8000:8000 chatbot-api
```

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.


