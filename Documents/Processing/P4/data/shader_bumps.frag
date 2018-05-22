#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  vec4 diffuse_color = texture2D(texture, vertTexCoord.st) * vertColor;
  vec4 diffuse_color2 = vec4(vec3(1, 1, 1) - diffuse_color.xyz, diffuse_color.a);
  gl_FragColor = vec4(diffuse_color2.rgb, 1.0);
}


