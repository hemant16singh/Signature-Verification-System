import os
import sys

def check_dataset():
    """Diagnostic tool to check dataset location"""
    print("=" * 50)
    print("🔍 DATASET DIAGNOSTIC TOOL")
    print("=" * 50)
    
    # Current working directory
    print(f"\n📂 Current working directory:")
    print(f"   {os.getcwd()}")
    
    # Check common locations
    print(f"\n🔎 Checking common dataset locations:")
    
    locations = [
        '.',
        '..',
        '../dataset',
        'dataset',
        './dataset',
        '../dataset/signatures',
        './dataset/signatures',
        'D:/signature1/signature-verification-flask/dataset',
        'D:/signature1/signature-verification-flask/dataset/signatures',
    ]
    
    found = False
    for loc in locations:
        full_path = os.path.abspath(loc)
        exists = os.path.exists(full_path)
        status = "✅" if exists else "❌"
        print(f"   {status} {full_path}")
        
        if exists and os.path.isdir(full_path):
            files = os.listdir(full_path)[:5]  # Show first 5 files/folders
            if files:
                print(f"      Contains: {', '.join(files)}")
            
            # Check for signature folders
            if 'full_org' in os.listdir(full_path) or 'full_forg' in os.listdir(full_path):
                found = True
                print(f"      ⭐ Found signature folders here!")
    
    if not found:
        print("\n⚠️  Could not find signature folders in checked locations")
        print("\n💡 Recommendations:")
        print("   1. Make sure you've downloaded the dataset from Kaggle")
        print("   2. Extract the dataset to: D:/signature1/signature-verification-flask/dataset/signatures/")
        print("   3. The structure should be:")
        print("      dataset/signatures/full_org/  (contains genuine signatures)")
        print("      dataset/signatures/full_forg/ (contains forged signatures)")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    check_dataset()