$("#add-cupcake-form").on("submit", addCupcake);

async function addCupcake(e) {
  e.preventDefault();
  const body = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val()
  };

  if ($("#image").val()) {
    body['image'] = $("#image").val()
  }

  let response = await axios.post("/api/cupcakes", body);
  console.log(response.data);
  renderCupcakesList();
}

$(document).ready(renderCupcakesList);

async function renderCupcakesList() {
  let response = await axios.get("/api/cupcakes");

  $(".cupcake-container").empty();
  for (let cupcake of response.data.cupcakes) {
    const { flavor, size, rating, image } = cupcake;
    const html = `
        <div class="cupcake-item">
            <img src='${image}' alt="cupcake" />
            <h2>Flavor: ${flavor}</h2>
            <h2>Size: ${size}</h2>
            <h2>Rating: ${rating}</h2>
        </div>
        `;

    $(".cupcake-container").append(html);
  }
}
