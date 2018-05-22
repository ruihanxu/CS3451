/* Datatype: */
	float, int, bool
	vec2 // 2D vector
	vec3 // 3D position, normal vector, rgb
	vec4 // (r,b,g,a)<- a for opacity
	mat3 // 3x3 matrix
	mat4 //4x4 matrix
	uniform sampler2D //texture map

/* Opeartions */
	+ - * / = += *= ++ --
	sin, cos, abs, floor, ceil, min, max, pow, sqrt, inversesqrt
	length, dot, cross, nomalize, reflect
	texture2D(sampler, texture, coord) -->rgb
 
/* Vertex Program for diffuse shader */
	// sent through rasterizar, to fragment shader
	varying vec3 normal;
	varying vec3 vertex_to_light; 
	
	void main() {
		gl_Position = transform * position; // CTM * vertex position, including projection

		normal = gl_NormalMatrix * gl_Normal;

		vec4 vertex_ModelView = gl_ModelViewMatrix * gl_Vertex; // 3D postion of vertex
		vertex_to_light = vec3(gl_LightSource[0].postion - vertex_ModelView);
}

/* Fragment Program */
	varying vec3 normal;
	varying vec3 vertex_to_light;

	void main() {
		const vec4 diffuse_color = vec4(1.0, 0.0, 0.0, 1.0) // rgba = opaque red

		vec3 n_normal = normalize(normal);
		vec3 n_vertex_to_light = normalize(vertex_to_light);
		float diffuse = clamp(dot(n_normal, n_vertex_to_light),0.0,1.0);

		gl_FragColor = diffuse * diffuse_color; // color = (N·L)red
	}

/* Swizzling */
	// address components of vectors with .xyzw, .rgba, .stpg
	vec4 v1 = vec4(4.0, -2.0, 5.0, 3.0); // xyzw
	vec2 v2 = v1.yz; // v2 = (-2,5)
	float scalar = v1.w; // scalar = 3
	vec3 v3 = v1.zzz; // v3 = (5,5,5)

/* Vertex Program - Twisting */
	void main() {
		vec4 pos = transform * position;
		vec4 center = vec4(512, 512, 0, 0);
		vec2 diff = vec2(pos.x - center.x, pos.y - center.y);
		float angle = twist * length(diff);
		float c = cos(angle);
		float s = sin(angle);

		// 2D rotation
		gl_Position.x = c * pos.x - s * pos.y;
		gl_Position.y = s * pos.x + c * pos.y;
		gl_Position.z = pos.z;
		gl_Position.w = pos.w;

		gl_FrontColor = gl_BackColor = gl_Color; // copy color to output
	}

/* Vertex Program - Texture */
	varying vec2 texture_coord;
	void main() {
		gl_Position = transform * position;
		texture.coord = vec2(gl_MultiTexCoord0);
	}

/* Fragment Program -Texture */
	varying vec2 texture_coord;
	uniform sampler2D my_color_textures;
	void main() {
		gl_FragColor = texture2D(my_color_textures, texture_coord);
	}

/* my_texture       final_image
 |--------|      |--------|
 |  \--\  |      |-\-\-\--|
 |   \  \ |   ==>|--\ \ \-|
 |    \--\|      |---\-\-\|
 |--------|      |--------| */
/* Vertex Program - Two Textures */
 	varying vec2 left_coord;
 	varying vec2 right_coord;
 	void main(){
 		gl_Position = transform * position; // transform == gl_ModelViewProjectionMatrix in pure GLSL
 		vec2 texture_coord = vec2(gl_MultiTexCoord0);
 		left_coord = texture_coord + vec2(-0.2, 0.0);
 		right_coord = texture_coord + vec2(0.2, 0.0);
 	}
/* Fragment Program - Two Textures */
	varying vec2 left_coord;
	varying vec2 right_coord;
	uniform sampler2D my_texture;
	void main() {
		vec4 leftColor = texture2D(my_texture, left_coord);
		vec4 rightColor = texture2D(my_texture, right_coord);
		gl_FragColor = 0.5 * (leftColor + rightColor);
	}






