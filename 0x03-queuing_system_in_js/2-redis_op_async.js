import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

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
  const value = await getAsync(schoolName);
  if (value) console.log(value);
};

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
