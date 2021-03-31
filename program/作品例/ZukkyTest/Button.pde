
class Button {
  float x, y, w, h ;
  private boolean cmp = false ;
  
  Button(float  x, float y, float w, float h) {
    this.x = x ; this.y = y ; 
    this.h = h ; this.w = w ;
  }
  
  void view() {
    if(x < mouseX && mouseX < x + w && y < mouseY && mouseY < y + h && mousePressed)
      fill(#ff00ff) ;
    else 
      fill(#00ff00) ;
    rect(x, y, w, h) ;
  }
  
  boolean isClick() {
    boolean b = x < mouseX && mouseX < x + w && y < mouseY && mouseY < y + h && cmp && !mousePressed ;
    cmp = mousePressed ;
    return b ;
  }
  
}