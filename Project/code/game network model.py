class ICGNetwork:
    """ICG游戏网络：支持复杂的游戏关系"""
    
    def __init__(self):
        self.games = {}
        self.connections = {}
        self.manager = ICGManager()
    
    def add_game(self, game_id: str, game: ICGGame):
        self.games[game_id] = game
    
    def connect_games(self, source_id: str, target_id: str, condition=None):
        """连接两个游戏，当条件满足时可以切换"""
        if source_id not in self.connections:
            self.connections[source_id] = []
        
        self.connections[source_id].append({
            'target': target_id,
            'condition': condition or (lambda g: g.is_terminal())
        })
    
    def get_available_games(self, current_game_id: str):
        """获取当前可玩的游戏"""
        available = [current_game_id]
        
        if current_game_id in self.connections:
            for connection in self.connections[current_game_id]:
                current_game = self.games[current_game_id]
                if connection['condition'](current_game):
                    available.append(connection['target'])
        
        return available
    
    def play_network(self, start_game_id: str):
        """在游戏网络中游玩"""
        current_game_id = start_game_id
        move_history = []
        
        while True:
            current_game = self.games[current_game_id]
            print(f"\n当前游戏: {current_game_id}")
            print(f"Grundy数: {current_game.get_grundy_number()}")
            
            if current_game.is_terminal():
                print("游戏结束!")
                break
            
            # 获取可用的游戏
            available_games = self.get_available_games(current_game_id)
            if len(available_games) > 1:
                print(f"可切换的游戏: {available_games}")
            
            # 简化：只玩当前游戏
            moves = current_game.get_legal_moves()
            if not moves:
                break
            
            # 这里可以添加AI或玩家输入
            move = moves[0]  # 简化：选择第一个移动
            self.games[current_game_id] = current_game.make_move(move)
            move_history.append((current_game_id, move))
        
        return move_history

# 使用示例
def create_complex_icg_network():
    network = ICGNetwork()
    
    # 添加各种游戏
    network.add_game("nim1", NimGame([3, 4, 5]))
    network.add_game("nim2", NimGame([2, 2]))
    network.add_game("sub1", SubtractionGame(7))
    network.add_game("sub2", SubtractionGame(10))
    
    # 创建连接关系
    network.connect_games("nim1", "sub1")
    network.connect_games("sub1", "nim2", condition=lambda g: g.stones <= 3)
    network.connect_games("nim2", "sub2")
    
    return network

# 运行游戏网络
network = create_complex_icg_network()
history = network.play_network("nim1")
print(f"\n游戏历史: {history}")