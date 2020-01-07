let elements = document.querySelectorAll("a.translate_link");

elements.forEach(element => {
  element.addEventListener("click", translate);
});

function translate() {
  let id = this.parentNode.id;
  id = id.replace(/\D/g, "");
  let post = document.getElementById("post" + id);
  let data = {
    source_lang: "en",
    target_lang: "tr",
    post_org_text: post.textContent
  };

  fetch("/translate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then(data => {
      if (data.length > 0) {
        post.prepend(data.text, document.createElement("br"));
        this.remove();
      }
    })
    .catch(error => {
      console.error(("Error", error));
    });
}
