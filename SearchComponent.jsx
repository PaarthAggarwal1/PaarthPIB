import { useEffect, useState } from "react";

function UserSearch() {
    const [search, setSearch] = useState("");
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    useEffect(() => {
        if (search.trim() === "") {
            setUsers([]);
            setError("");
            return;
        }

        let active = true;

        const timer = setTimeout(() => {
            setLoading(true);
            setError("");

            fetch(`/api/users?search=${search}`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Request failed");
                    }

                    return response.json();
                })
                .then((data) => {
                    if (active) {
                        setUsers(data);
                    }
                })
                .catch(() => {
                    if (active) {
                        setError("Unable to load users");
                        setUsers([]);
                    }
                })
                .finally(() => {
                    if (active) {
                        setLoading(false);
                    }
                });
        }, 500);

        return () => {
            clearTimeout(timer);
            active = false;
        };
    }, [search]);

    return (
        <div>
            <h2>User Search</h2>

            <input
                type="text"
                placeholder="Search"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />

            {loading && <p>Loading...</p>}

            {error && <p>{error}</p>}

            {!loading && !error && search && users.length === 0 && (
                <p>No users found</p>
            )}

            {users.length > 0 && (
                <ul>
                    {users.map((user) => (
                        <li key={user.id}>{user.name}</li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default UserSearch;