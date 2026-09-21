const loadButton = document.getElementById('loadPolicies');
const policyList = document.getElementById('policyList');

async function fetchPolicies() {
  try {
    const response = await fetch('http://localhost:8000/api/policies');
    const data = await response.json();

    policyList.innerHTML = '';
    data.forEach((policy) => {
      const item = document.createElement('li');
      item.textContent = `${policy.name} — ${policy.type} — $${policy.premium}/mo`;
      policyList.appendChild(item);
    });
  } catch (error) {
    policyList.innerHTML = '<li>Unable to load policies. Start the backend server first.</li>';
    console.error(error);
  }
}

loadButton.addEventListener('click', fetchPolicies);
