window.addEventListener("upload", function(){
	document.querySelector('input[type="file"]').addEventListener("change", function() {
		if (this.files && this.files[0]) {
			var img = document.querySelector('img');
			img.onload = () => {
				URL.revokeObjectURL(img.src); // no longer needed, free memory
			}

			img.src = URLcreateObjectURL(this.files[0]); // set src to blob url
		}
	});
});
