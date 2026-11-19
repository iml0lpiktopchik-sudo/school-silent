from kivy.app import App
from kivy.clock import Clock
from plyer import gps
from jnius import autoclass, cast
from android.permissions import request_permissions, Permission
import math

# Координаты школы (ЗАМЕНИТЕ НА СВОИ)
SCHOOL_LAT = 55.7558
SCHOOL_LON = 37.6173
RADIUS_METERS = 100  # Радиус в метрах

class SchoolSilentApp(App):
    def build(self):
        # Запрашиваем разрешения при запуске
        request_permissions([
            Permission.ACCESS_FINE_LOCATION,
            Permission.ACCESS_COARSE_LOCATION,
            Permission.ACCESS_BACKGROUND_LOCATION
        ])
        
        # Запускаем GPS
        try:
            gps.configure(on_location=self.on_location)
            gps.start(minTime=10000, minDistance=10) # Обновление каждые 10 сек
            print("DEBUG: GPS запущен")
        except NotImplementedError:
            print("DEBUG: GPS не поддерживается")
        except Exception as e:
            print(f"DEBUG: Ошибка GPS: {e}")

        return None # Интерфейс не нужен

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        if lat is None or lon is None:
            return

        dist = self.haversine(lat, lon, SCHOOL_LAT, SCHOOL_LON)
        print(f"DEBUG: Расстояние: {dist:.1f} м")

        if dist <= RADIUS_METERS:
            self.set_ringer_mode(True)
        else:
            self.set_ringer_mode(False)

    def set_ringer_mode(self, silent):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            AudioManager = autoclass('android.media.AudioManager')
            
            activity = PythonActivity.mActivity
            audio_manager = cast('android.media.AudioManager',
                                 activity.getSystemService(Context.AUDIO_SERVICE))
            
            if silent:
                audio_manager.setRingerMode(0) # 0 = Беззвучный
                print("DEBUG: Включен беззвучный режим")
            else:
                audio_manager.setRingerMode(2) # 2 = Обычный
                print("DEBUG: Восстановлен обычный режим")
        except Exception as e:
            print(f"DEBUG: Ошибка переключения: {e}")

    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371000
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

if __name__ == '__main__':
    SchoolSilentApp().run()
