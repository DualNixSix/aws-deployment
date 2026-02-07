const BASE_URL = window.location.protocol + '//' + window.location.host;

const basicFetch = async (url, context) => {
  try {
    const response = await fetch(url, context);

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`HTTP Error ${response.status}: ${errorText}`);
    }

    const body = await response.json();
    return body;
  } catch (error) {
    console.error("Failed to fetch:", error.message);
    throw error;
  }
};

const getCredentials = (e) => {
  const uname = e.target.uname.value;
  const pword = e.target.password.value;
  return [uname, pword];
};

const writePokemonApi = (body) => {
  const container = document.querySelector("#pokemon-list");
  if (!body || !body.length) {
    alert("You must log in first!");
    return;
  }
  container.innerHTML = "";
  body.forEach((pokemon, i) => {
    const block = document.createElement("div");
    block.innerHTML = `
      <h4>Pokemon ${i + 1}: ${pokemon.fields.name}</h4>
      <p>Description: ${pokemon.fields.description}</p>
      <p>Moves: ${pokemon.fields.moves.map(m => m.fields.name).join(", ")}</p>
    `;
    container.appendChild(block);
  });
};

const handleAuth = async (e) => {
  e.preventDefault();
  const [uname, pword] = getCredentials(e);
  const checkbox = document.querySelector("#signup");
  if (checkbox.checked) {
    signUp(uname, pword);
  } else {
    const token = await getToken(uname, pword);
    localStorage.setItem("token", token);
  }
};

const signUp = (uname, pword) => {
  const data = { username: uname, password: pword };
  const context = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  return basicFetch(`${BASE_URL}/api/accounts/signup`, context);
};

const getToken = async (uname, pword) => {
  const data = { username: uname, password: pword };
  const context = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  const body = await basicFetch(`${BASE_URL}/api/accounts/get-token`, context);
  return body["token"];
};

const fetchResults = async () => {
  const token = localStorage.getItem("token");
  const context = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Token ${token}`,
    },
  };
  return basicFetch(`${BASE_URL}/api/v1/pokemon/`, context);
};

window.onload = () => {
  const form = document.querySelector("#form");
  const getInfo = document.querySelector("#getinfo");
  const logout = document.querySelector("#logout-btn");

  form.onsubmit = (e) => handleAuth(e);
  getInfo.onclick = async () => {
    const body = await fetchResults();
    writePokemonApi(body);
  };
  logout.onclick = () => localStorage.removeItem("token");
};
