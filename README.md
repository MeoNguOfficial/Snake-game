VIETNAMESE - TIẾNG VIỆT
Cài đặt Python
Truy cập trang web chính thức của Python tại python.org.
Tải về phiên bản Python mới nhất phù hợp với hệ điều hành của bạn.

Cài đặt PyGame:
Mở Command Prompt (Windows) hoặc Terminal (macOS/Linux).
Gõ lệnh sau để cài đặt PyGame:
PowerShell or Terminal: pip install pygame

Tạo thư mục Resources vào trong Game1 (có thể thay tên nếu cần, nếu thay hãy tìm dòng này:)

eat_food_sound = pygame.mixer.Sound("../Game1/Resources/eat_food.mp3")
pause_game_sound = pygame.mixer.Sound("../Game1/Resources/pause_game.mp3")
high_score_sound = pygame.mixer.Sound("../Game1/Resources/high_score.mp3")
invert_control_sound = pygame.mixer.Sound("../Game1/Resources/invert_control.mp3")
game_over_sound = pygame.mixer.Sound("../Game1/Resources/game_over.mp3")

# Tải nhạc nền
pygame.mixer.music.load("../Game1/Resources/start_game.mp3")
pygame.mixer.music.set_volume(0.5)  # Điều chỉnh âm lượng nếu cần

Cuối cùng nhập 
python Snake.py

Nếu cửa sổ game hiện lên, tức là cài đặt Python và PyGame đã thành công.


ENGLISH

Installing Python

Go to the official Python website at python.org.
Download the latest version of Python that is compatible with your operating system.
Installing PyGame:

Open the Command Prompt (Windows) or Terminal (macOS/Linux).
Type the following command to install PyGame:
PowerShell or Terminal: pip install pygame
Create a Resources folder inside the Game1 directory (you can change the name if needed, and if you do, make sure to update the following lines accordingly):

eat_food_sound = pygame.mixer.Sound("../Game1/Resources/eat_food.mp3")
pause_game_sound = pygame.mixer.Sound("../Game1/Resources/pause_game.mp3")
high_score_sound = pygame.mixer.Sound("../Game1/Resources/high_score.mp3")
invert_control_sound = pygame.mixer.Sound("../Game1/Resources/invert_control.mp3")
game_over_sound = pygame.mixer.Sound("../Game1/Resources/game_over.mp3")

Load the background music
pygame.mixer.music.load("../Game1/Resources/start_game.mp3")
pygame.mixer.music.set_volume(0.5) # Adjust the volume if needed

Finally, run the game by entering:
python Snake.py

If the game window appears, it means that the installation of Python and PyGame was successful.
