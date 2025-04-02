import requests
import json

BASE_URL = "http://127.0.0.1:8000"  # Sesuaikan dengan API

def generate_atomic_topics():
    topic = input("Masukkan topik yang ingin dianalisis: ")
    payload = {"given_topic": topic}
    
    response = requests.post(f"{BASE_URL}/generate-topics", json=payload)
    if response.status_code == 200:
        print("✅ Hasil:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

def start_session():
    topic = input("Masukkan atomic topic: ")
    explanation = input("Masukkan penjelasan awal: ")
    payload = {
        "atomic_topic": topic,
        "initial_explanation": explanation
    }
    
    response = requests.post(f"{BASE_URL}/start-session", json=payload)
    if response.status_code == 200:
        result = response.json()
        goal = result["goal"]
        print("\n✅ Session Dimulai!")
        print(f"🎯 Learning Goal: {goal}")
        return goal  # Return goal untuk digunakan di submit_explanation()
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return None

def submit_explanation(goal):
    print("\n⚡ Mulai menjelaskan... (Looping sampai goal tercapai)")
    
    while True:
        explanation = input("\nMasukkan penjelasanmu: ")
        payload = {"explanation": explanation, "goal": goal}
        
        response = requests.post(f"{BASE_URL}/submit-explanation", json=payload)
        if response.status_code == 200:
            result = response.json()
            print(json.dumps(result, indent=4))

            if result["is_goal_met"]:
                print("\n🎉 Goal Tercapai! Belajar selesai.")
                break
            else:
                print("\n🔁 Goal belum tercapai, coba jelaskan lagi dengan memperbaiki berdasarkan feedback.")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            break

def main():
    while True:
        print("\n=== Feynman API CLI Tester ===")
        print("1. Generate Atomic Topics")
        print("2. Start Learning Session & Submit Explanation")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1-3): ")
        
        if choice == "1":
            generate_atomic_topics()
        elif choice == "2":
            goal = start_session()
            if goal:
                submit_explanation(goal)
        elif choice == "3":
            print("Keluar dari CLI...")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
