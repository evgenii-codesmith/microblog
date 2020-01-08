function translate(post_id, source_language, target_language, post_content) {
  let post = document.getElementById("post" + post_id);
  let translate = document.getElementById("translation" + post_id);
  let data = {
    source_lang: source_language,
    target_lang: target_language,
    post_org_text: post_content
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
      if (data.text != "error") {
        post.prepend(data.text, document.createElement("br"));
        translate.remove();
      }
    })
    .catch(error => {
      console.error(("Error", error));
    });
}
