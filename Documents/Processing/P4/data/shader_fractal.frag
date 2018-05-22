#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

vec2 MultV(vec2 z, vec2 c);

void main() {
  	float x0 = vertTexCoord.s*6-2;
	float y0 = vertTexCoord.t*6-3;
	float x = 0.5;
	float y = 0.0;

	int iteration = 0;
	int max_iteration = 20;

	// vec2 z = vec2(x,y);
	// vec2 c = vec2(x0,y0);

	// vec2 one_minus_z, cz, res;

	float new_x,new_y,final_x, final_y;

	while (iteration < max_iteration) {
		// z(i+1) = c * z(i) * (1 – z）
		// cz = MultV(c,z);
		// one_minus_z = vec2(1-x, y);
		// res = MultV(cz,one_minus_z);
		// z = res;

		// c*z
		new_x = x0*x - y0*y;
		new_y = x0*y + y0*x;
		// c*z*(1-z),1-z = 1-x,y
		final_x = new_x*(1-x) - new_y*-y;
		final_y = new_x*-y + new_y*(1-x);

		x = final_x;
		y = final_y;


		iteration = iteration + 1;
	}
	if (x*x + y*y <= 2*2)
		gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
	else
		gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}

vec2 MultV(vec2 z, vec2 c) {
	float a = z.x*c.x - z.y*c.y;
	float b = z.x*c.y + z.y*c.x;
	return vec2(a,b);
}



