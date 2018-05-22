#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
	float thisx = vertTexCoord.x;
	float thisy = vertTexCoord.y;
	float c = 0.005;

	vec4 p = texture2D(texture, vec2(thisx, thisy));

	vec4 p1 = texture2D(texture, vec2(thisx-c*2, thisy));
	vec4 p2 = texture2D(texture, vec2(thisx+c*2, thisy));
	vec4 p3 = texture2D(texture, vec2(thisx-c, thisy));
	vec4 p4 = texture2D(texture, vec2(thisx+c, thisy));
	vec4 p5 = texture2D(texture, vec2(thisx-c*3, thisy));
	vec4 p6 = texture2D(texture, vec2(thisx+c*3, thisy));
	vec4 p7 = texture2D(texture, vec2(thisx-c*4, thisy));
	vec4 p8 = texture2D(texture, vec2(thisx+c*4, thisy));
	vec4 p9 = texture2D(texture, vec2(thisx-c*5, thisy));
	vec4 p10 = texture2D(texture, vec2(thisx+c*5, thisy));
	vec4 p11 = texture2D(texture, vec2(thisx-c*6, thisy));
	vec4 p12 = texture2D(texture, vec2(thisx+c*6, thisy));
	vec4 p13 = texture2D(texture, vec2(thisx-c*7, thisy));
	vec4 p14 = texture2D(texture, vec2(thisx+c*7, thisy));
	vec4 p15 = texture2D(texture, vec2(thisx-c*8, thisy));
	vec4 p16 = texture2D(texture, vec2(thisx+c*8, thisy));
	vec4 p17 = texture2D(texture, vec2(thisx-c*9, thisy));
	vec4 p18 = texture2D(texture, vec2(thisx+c*9, thisy));
	vec4 p19 = texture2D(texture, vec2(thisx-c*10, thisy));
	vec4 p20 = texture2D(texture, vec2(thisx+c*10, thisy));

	float r = (p1.r + p2.r + p3.r + p4.r + p5.r + p6.r + p7.r + p8.r + p9.r + p10.r 
		+ p11.r + p12.r + p13.r + p14.r + p15.r + p16.r + p17.r + p18.r + p19.r + p20.r+ p.r)/21.0;
	float g = (p1.g + p2.g + p3.g + p4.g + p5.g + p6.g + p7.g + p8.g + p9.g + p10.g + p11.g + p12.g 
		+ p13.g + p14.g + p15.g + p16.g + p17.g + p18.g + p19.g + p20.g + p.g)/21.0;
	float b = (p1.b + p2.b + p3.b + p4.b + p5.b + p6.b + p7.b + p8.b + p9.b + p10.b + p11.b + p12.b
	 	+ p13.b + p14.b + p15.b + p16.b + p17.b + p18.b + p19.b + p20.b + p.b)/21.0;

	vec4 avg = vec4(r,g,b, 1.0);
	gl_FragColor = vec4(avg.rgb, 1.0);
}

