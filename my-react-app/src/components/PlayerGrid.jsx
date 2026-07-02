import players from "../data/players.json";
import PlayerCard from '../components/PlayerCard'
import '../css/PlayerGrid.css'

function PlayerGrid() {
  console.log(players);

  return (
    <main>
      <h1>U-22 FIFA World Cup Players</h1>
      <p>Total players: {players.length}</p>

      <section className="player-grid">
        {players.map((player, index) => (
          <PlayerCard key={index} player={player} />
        ))}

      </section>
    </main>
  );
}

export default PlayerGrid