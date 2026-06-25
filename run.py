from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Starting Signature Verification System")
    print("=" * 50)
    print(f"✅ Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"   {rule.endpoint}: {rule.rule}")
    print("=" * 50)
    print("🌐 Access the application at: http://localhost:5000")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)