document.getElementById("calculateButton").
  addEventListener("click", async () => {
    const value1 = parseFloat(document.getElementById("value1").value);
    const value2 = parseFloat(document.getElementById("value2").value);
    const operation = document.getElementById("operation").value;

    try {
      const endpoint = "http://127.0.0.1:8000/calculate";
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value1, value2, operation })
      });

      console.log(response)
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "An unknown error occurred");
      }

      const data = await response.json();
      document.getElementById("result").textContent = data.result;

    } catch (error) {
      document.getElementById("result").textContent = "Error!";
      console.error(error);
    }
  });
