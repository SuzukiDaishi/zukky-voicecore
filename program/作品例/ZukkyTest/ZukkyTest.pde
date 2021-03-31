
Button b = new Button(50,50, 150, 150) ; 

void setup() {
  size(250, 250);
  speakAsync("ボタンを押してね") ;
}

void draw() {
  if(b.isClick()) 
    speakAsync("ハロー") ;
  b.view() ;
}


void speakAsync(String text) {
  try {
    Runtime.getRuntime().exec(new String[]{"/Users/suzukidaishi/Desktop/VoiceKit/VoiceKitAPI.sh", text.replace("\n","")}) ;
  } catch (Exception e) {
    print("なんかエラー") ;
  }
}