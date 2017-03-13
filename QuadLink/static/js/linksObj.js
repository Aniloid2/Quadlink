function links(axis,pitch,roll,yaw,ip_address,acceleration,x_acc,y_acc,z_acc, thrust) {
	this.axis = axis;
	this.pitch = pitch;
	this.roll = roll;
	this.yaw = yaw;
	this.ip_address = ip_address;
	this.acceleration= acceleration;
	this.x_acc = x_acc;
	this.y_acc = y_acc;
	this.z_acc = z_acc;
	this.thrust = thrust
}



function scenary(shape,scene,camera,renderer){
	this.shape = shape;
	this.scene = scene;
	this.camera = camera;
	this.renderer = renderer;
}