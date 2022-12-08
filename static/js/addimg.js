document.querySelector("#file").addEventListener("change", (e) => { 
    if (window.File && window.FileReader && window.FileList && window.Blob) { 
      const files = e.target.files;   
      for (let i = 0; i < files.length; i++) { // LOOP THROUGH THE FILE LIST OBJECT
        var error = document.getElementById("error");
          if (files.length >= 5) {
            setTimeout(() => {
              error.style.display = "none";
            }, "5000")
            error.textContent = "Будь ласка, додайте до 4 фотографій."
            error.style.display = "flex";
            continue;
          }
          else if (!files[i].type.match("image")){
            setTimeout(() => {
              error.style.display = "none";
            }, "5000")
            error.textContent = "Підтримуються лише файли типу png, jpeg або jpg."
            error.style.display = "flex";
            continue;
          }
          const picReader = new FileReader(); // RETRIEVE DATA URI 
          var element = document.getElementById("contentBox");
          while (element.firstChild) {
            element.removeChild(element.firstChild);
          }
          picReader.addEventListener("load", function (event) { // LOAD EVENT FOR DISPLAYING PHOTOS
  
            
            var img = document.createElement("img");
            var src = document.getElementById("contentBox");
            const picFile = event.target;
            // console.log(picFile.result)
            // img.innerHTML = `<img class="col-6" src="${picFile.result}" title="${picFile.name}"/>`;
            img.src = picFile.result
            // img.src = URL.createObjectURL(picFile.result);
            // img.style.imageRendering = "url("+ picFile.result +")";
            img.classList.add("col-6");
            src.appendChild(img);
          });
          picReader.readAsDataURL(files[i]); //READ THE IMAGE
      }
    } else {
      alert("Your browser does not support File API");
    }
  });