from predictor import PicoPlacaPredictor

if __name__ == "__main__":
    predictor = PicoPlacaPredictor()

    plate = input("Ingresa la placa (ej. PBC-1234): ").strip()
    date = input("Ingresa la fecha (YYYY-MM-DD): ").strip()
    time = input("Ingresa la hora (HH:MM, 24h): ").strip()

    try:
        if predictor.can_drive(plate, date, time):
            print("Puede circular!!!")
        else:
            print("No puede circular X!")
    except Exception as e:
        print(f"Error: {e}")
