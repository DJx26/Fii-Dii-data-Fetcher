from pyngrok import ngrok

# Disconnect old tunnels
for tunnel in ngrok.get_tunnels():
    ngrok.disconnect(tunnel.public_url)
public_url = ngrok.connect(8501)
print("🌐 App is live at:", public_url)
