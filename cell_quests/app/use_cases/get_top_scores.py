class GetScoreboard:
    def get_scoreboard(self):
        # Método existente para obter o ranking
        pass

    def get_top_scores(self, limit=5):
        query = "SELECT username, score FROM scoreboard ORDER BY score DESC LIMIT %s"
        cursor.execute(query, (limit,))
        result = cursor.fetchall()
        return [{'username': row[0], 'score': row[1]} for row in result]
