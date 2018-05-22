#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float s = vertTexCoord.s;
  s = (s-int(s)) * 2 - 1.0;

  float t = vertTexCoord.t;
  t = (t-int(t))*2 - 1.0;

  float square = t*t + s*s;

  if (square < 0.01){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 0.04) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 0.09) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 0.16) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 0.25) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 0.36) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 0.49) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 0.64) {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 0.81){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 1.00){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 1.21){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else if (square < 1.44){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  } else if (square < 1.69){
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.8);
  } else {
  	gl_FragColor = vec4(0.2, 0.4, 1.0, 0.0);
  }

}

