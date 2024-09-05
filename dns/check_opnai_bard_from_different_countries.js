// Get the IP addresses of Bard and OpenAI
const bard_ip = `https://api.ipify.org/`;
const openai_ip = `https://api.ipify.org/`;

// Check if the IP addresses are reachable from Italy, France, Canada, and the United States
for (const country of ["IT", "FR", "CA", "US"]) {
  try {
    const response = fetch(`http://${bard_ip}/api/v1/engines/bard`, {
      timeout: 10,
    });
    if (response.status === 200) {
      console.log(`Bard is reachable from ${country}`);
    } else {
      console.log(`Bard is not reachable from ${country}`);
    }
  } catch (error) {
    console.log(`Bard is not reachable from ${country}`);
  }

  try {
    const response = fetch(`http://${openai_ip}/api/v1/engines/davinci`, {
      timeout: 10,
    });
    if (response.status === 200) {
      console.log(`OpenAI is reachable from ${country}`);
    } else {
      console.log(`OpenAI is not reachable from ${country}`);
    }
  } catch (error) {
    console.log(`OpenAI is not reachable from ${country}`);
  }
}
