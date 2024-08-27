import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = async (schoolName, value) => {
  try {
    client.set(schoolName, value, print);
  } catch (error) {
    console.error(`Failed to set ${schoolName}: ${error.message}`);
  }
};

const displaySchoolValue = async (schoolName) => {
  try {
    client.get(schoolName, (err, value) => {
      if (err) {
        console.error(`Failed to get ${schoolName}: ${err.message}`);
      } else {
        console.log(value);
      }
    });
  } catch (error) {
    console.error(`Failed to get ${schoolName}: ${error.message}`);
  }
};

// Example usage
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
