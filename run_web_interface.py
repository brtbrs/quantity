#!/usr/bin/env python3
"""
Trading System Web Interface Launcher
Run this script to start the FastAPI web server with frontend
"""

import subprocess
import sys
import os
import webbrowser
import time
import threading

def main():
    """Launch the web interface"""
    print("🚀 Starting Trading System Web Interface...")
    print("📊 Web interface will be available at http://localhost:8000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set up environment
    os.environ['PYTHONPATH'] = script_dir
    
    try:
        # Start the FastAPI server
        server_process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "data_service.web.api_server:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload"
        ])
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Open browser
        def open_browser():
            time.sleep(2)  # Wait a bit more for server to be ready
            try:
                webbrowser.open('http://localhost:8000')
                print("🌐 Browser opened automatically")
            except:
                print("🌐 Please open http://localhost:8000 in your browser")
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        print("✅ Web interface is running!")
        print("📱 You can access it from any device on your network")
        print("🔗 Local: http://localhost:8000")
        print("🔗 Network: http://0.0.0.0:8000")
        
        # Wait for server to finish
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\n⏹️  Web interface stopped by user")
        if 'server_process' in locals():
            server_process.terminate()
    except Exception as e:
        print(f"❌ Error starting web interface: {e}")
        print("💡 Make sure you have installed the required dependencies:")
        print("   pip install fastapi uvicorn")

if __name__ == "__main__":
    main() 