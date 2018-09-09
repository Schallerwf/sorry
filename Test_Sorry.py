import unittest
from Sorry import *

SAMPLE_PAWN_SETUP = {Y: ["board:4", "board:59", "start", "start"],
                     G: ["start", "board:30", "safe:1", "start"],
                     R: ["start", "start", "home", "start"],
                     B: ["start", "safe:1", "start", "board:13"],}

class TestBoard(unittest.TestCase):
    def test_pawnAtLocation(self):
        board = Board()
        self.assertEqual(None, board.pawnAtLocation(SAMPLE_PAWN_SETUP, "board:1"))
        self.assertEqual(Y, board.pawnAtLocation(SAMPLE_PAWN_SETUP, "board:4"))
        self.assertEqual(B, board.pawnAtLocation(SAMPLE_PAWN_SETUP, "board:13"))

    def test_opponentPawnsInPlay(self):
        board = Board()
        board.setPawns(SAMPLE_PAWN_SETUP)
        self.assertEqual(["board:30", "board:13"], board.opponentPawnsInPlay(Y))
        self.assertEqual(["board:4", "board:59", "board:13"], board.opponentPawnsInPlay(G))
        self.assertEqual(["board:4", "board:59", "board:30", "board:13"], board.opponentPawnsInPlay(R))
        self.assertEqual(["board:4", "board:59", "board:30"], board.opponentPawnsInPlay(B))

    def test_pawnsInPlay(self):
        board = Board()
        board.setPawns(SAMPLE_PAWN_SETUP)
        self.assertEqual(["board:4", "board:59"], board.pawnsInPlay(Y))
        self.assertEqual(["board:30", "safe:1"], board.pawnsInPlay(G))
        self.assertEqual([], board.pawnsInPlay(R))
        self.assertEqual(["safe:1", "board:13"], board.pawnsInPlay(B))
        self.assertEqual(["board:13"], board.pawnsInPlay(B, includeSafe=False))

    def test_numPawnsAtStart(self):
        board = Board()
        board.setPawns(SAMPLE_PAWN_SETUP)
        self.assertEqual(2, board.numPawnsAtStart(Y))
        self.assertEqual(2, board.numPawnsAtStart(G))
        self.assertEqual(3, board.numPawnsAtStart(R))
        self.assertEqual(2, board.numPawnsAtStart(B))

    def test_swap(self):
        board = Board()
        board.setPawns(SAMPLE_PAWN_SETUP)
        result = board.swap(G, "board:30", "board:59")
        self.assertEqual(
            {Y: ["board:4", "board:30", "start", "start"],
             G: ["start", "board:59", "safe:1", "start"],
             R: ["start", "start", "home", "start"],
             B: ["start", "safe:1", "start", "board:13"],},
            result)

        # G swaps with Y's first pawn, then slides, bumping a B pawn and another Y pawn
        # The swapped Y pawn will also then slide
        board.setPawns({Y: ["board:1", "board:4", "start", "start"],
                        G: ["start", "board:16", "start", "start"],
                        R: ["start", "start", "home", "start"],
                        B: ["start", "board:3", "start", "start"],})
        result = board.swap(G, "board:16", "board:1")
        self.assertEqual(
            {Y: ["board:19", "start", "start", "start"],
             G: ["start", "board:4", "start", "start"],
             R: ["start", "start", "home", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # G swaps with a Y pawn, G then slides, bumping the Y pawn that was just swapped
        board.setPawns({Y: ["board:1", "start", "start", "start"],
                        G: ["start", "board:2", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.swap(G, "board:2", "board:1")
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["start", "board:4", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # G swaps with a Y pawn, Y then slides, bumping the G pawn that was just swapped
        # This is a self destructive swap
        board.setPawns({Y: ["board:1", "start", "start", "start"],
                        G: ["start", "board:2", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.swap(Y, "board:1", "board:2")
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["start", "board:4", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

    def test_sorry(self):
        board = Board()
        board.setPawns(SAMPLE_PAWN_SETUP)
        result = board.sorry(G, "board:13")
        self.assertEqual(
            {Y: ["board:4", "board:59", "start", "start"],
             G: ["board:13", "board:30", "safe:1", "start"],
             R: ["start", "start", "home", "start"],
             B: ["start", "safe:1", "start", "start"],},
            result)

        # G sorrys Y's first pawn, then slides, bumping a B pawn and another Y pawn
        board.setPawns({Y: ["board:1", "board:4", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "home", "start"],
                        B: ["start", "board:3", "start", "start"],})
        result = board.sorry(G, "board:1")
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:4", "start", "start", "start"],
             R: ["start", "start", "home", "start"],
             B: ["start", "start", "start", "start"],},
            result)

    def test_startPawn(self):
        board = Board()
        # Start pawn for Y
        result = board.startPawn(Y)
        self.assertEqual(
            {Y: ["board:4", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)
        board.setPawns(result)

        # Starting another pawn for Y is invalid
        result = board.startPawn(Y)
        self.assertEqual(None, result)

        # Start pawn for G, bumping an R pawn back to start
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["board:19", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.startPawn(G)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:19", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

    def test_movePawn_into_safe_zone(self):
        board = Board()
        board.setPawns({Y: ["board:1", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["safe:1", "start", "start", "start"],})
        result = board.movePawn(Y, "board:1", 2)
        self.assertEqual(
            {Y: ["safe:1", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["safe:1", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["board:2", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:2", 1)
        self.assertEqual(
            {Y: ["safe:1", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:17", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:17", 1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["safe:1", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["board:2", "safe:2", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:2", 2)
        self.assertEqual(None, result)

    def test_movePawn_out_of_safe_zone(self):
        board = Board()
        board.setPawns({Y: ["safe:2", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:2", -4)
        self.assertEqual(
            {Y: ["board:0", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["safe:1", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:1", -1)
        self.assertEqual(
            {Y: ["board:2", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)


        board = Board()
        board.setPawns({Y: ["safe:1", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:1", -4)
        self.assertEqual(
            {Y: ["board:59", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Bump opponent back to start
        board = Board()
        board.setPawns({Y: ["safe:1", "start", "start", "start"],
                        G: ["board:59", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:1", -4)
        self.assertEqual(
            {Y: ["board:59", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Invalid move, cannot bump own pawn
        board = Board()
        board.setPawns({Y: ["safe:1", "board:59", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:1", -4)
        self.assertEqual(None, result)

    def test_movePawn_home(self):
        board = Board()
        board.setPawns({Y: ["start", "start", "home", "board:2"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:2", 11)
        self.assertEqual(
            {Y: ["start", "start", "home", "home"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "home", "safe:2"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:2", 4)
        self.assertEqual(
            {Y: ["start", "start", "home", "home"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "home", "safe:1"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "safe:1", 4)
        self.assertEqual(
            {Y: ["start", "start", "home", "safe:5"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

    def test_movePawn_slide(self):
        # Large Slide
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:4", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:4", 5)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:13", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Small Slide
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:0", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:0", 1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:4", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Don't slide on own color
        board = Board()
        board.setPawns({Y: ["board:0", "start", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:0", 1)
        self.assertEqual(
            {Y: ["board:1", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Bump pawns on slide, even if they are own color
        board = Board()
        board.setPawns({Y: ["start", "start", "board:3", "start"],
                        G: ["board:0", "board:2", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "board:4"],})
        result = board.movePawn(G, "board:0", 1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:4", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:0", "board:2", "board:3", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "board:4"],})
        result = board.movePawn(G, "board:0", 1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:4", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Move backward onto slide
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:5", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:5", -4)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:4", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

    def test_movePawn_basic(self):
        # Cannot bump own pawn
        board = Board()
        board.setPawns({Y: ["board:0", "board:1", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:0", 1)
        self.assertEqual(None, result)

        # Bump opponent pawn
        board = Board()
        board.setPawns({Y: ["board:5", "start", "start", "start"],
                        G: ["start", "board:6", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:5", 1)
        self.assertEqual(
            {Y: ["board:6", "start", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Hop own pawn
        board = Board()
        board.setPawns({Y: ["board:0", "board:1", "start", "start"],
                        G: ["start", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:0", 2)
        self.assertEqual(
            {Y: ["board:2", "board:1", "start", "start"],
             G: ["start", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Hop opponent pawn
        board = Board()
        board.setPawns({Y: ["board:0", "start", "start", "start"],
                        G: ["start", "board:1", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(Y, "board:0", 2)
        self.assertEqual(
            {Y: ["board:2", "start", "start", "start"],
             G: ["start", "board:1", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Move past opponent safe zones
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:0", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:0", 11)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:11", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Wrap around forward
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:59", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:59", 1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:0", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        # Wrap around backward
        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:0", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:0", -1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:59", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:0", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:0", -4)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:56", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:3", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:3", -4)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:59", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

        board = Board()
        board.setPawns({Y: ["start", "start", "start", "start"],
                        G: ["board:40", "start", "start", "start"],
                        R: ["start", "start", "start", "start"],
                        B: ["start", "start", "start", "start"],})
        result = board.movePawn(G, "board:40", -1)
        self.assertEqual(
            {Y: ["start", "start", "start", "start"],
             G: ["board:43", "start", "start", "start"],
             R: ["start", "start", "start", "start"],
             B: ["start", "start", "start", "start"],},
            result)

class TestGame(unittest.TestCase):
    def test_game_compute_states_sorry(self):
        game = Game()
        result = game.computePossibleGameStates("sorry", Y)
        self.assertEqual([], result)

        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates("sorry", Y)
        self.assertEqual(
            [{Y: ["board:4", "board:59", "board:30", "start"],
              G: ["start", "start", "safe:1", "start"],
              R: ["start", "start", "home", "start"],
              B: ["start", "safe:1", "start", "board:13"],},
             {Y: ["board:4", "board:59", "board:13", "start"],
              G: ["start", "board:30", "safe:1", "start"],
              R: ["start", "start", "home", "start"],
              B: ["start", "safe:1", "start", "start"],}], 
            result)

    def test_game_compute_states_1(self):
        game = Game()
        result = game.computePossibleGameStates(1, Y)
        self.assertEqual(
            [{Y: ["board:4", "start", "start", "start"],
              G: ["start", "start", "start", "start"],
              R: ["start", "start", "start", "start"],
              B: ["start", "start", "start", "start"],},], 
            result)
        game.setPawns(result[0])
        result = game.computePossibleGameStates(1, R)
        self.assertEqual(
            [{Y: ["board:4", "start", "start", "start"],
              G: ["start", "start", "start", "start"],
              R: ["board:34", "start", "start", "start"],
              B: ["start", "start", "start", "start"],},], 
            result)
        game.setPawns(result[0])
        result = game.computePossibleGameStates(1, R)
        self.assertEqual(
            [{Y: ["board:4", "start", "start", "start"],
              G: ["start", "start", "start", "start"],
              R: ["board:35", "start", "start", "start"],
              B: ["start", "start", "start", "start"],},], 
            result)

    def test_game_compute_states_2(self):
        game = Game()
        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates(2, G)
        self.assertEqual(
            [{Y: ["board:4", "board:59", "start", "start"],
              G: ["board:19", "board:30", "safe:1", "start"],
              R: ["start", "start", "home", "start"],
              B: ["start", "safe:1", "start", "board:13"],},
             {Y: ["board:4", "board:59", "start", "start"],
              G: ["start", "board:32", "safe:1", "start"],
              R: ["start", "start", "home", "start"],
              B: ["start", "safe:1", "start", "board:13"],},
             {Y: ["board:4", "board:59", "start", "start"],
              G: ["start", "board:30", "safe:3", "start"],
              R: ["start", "start", "home", "start"],
              B: ["start", "safe:1", "start", "board:13"],}], 
            result)

    def test_game_compute_states_basic_number(self):
        # 3, 5, 8, and 12 have no special modifiers and are treated the same under the hood.
        # No need to test all of them.
        game = Game()
        result = game.computePossibleGameStates(3, Y)
        self.assertEqual([], result)

        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates(8, Y)
        self.assertEqual([{Y: ["board:12", "board:59", "start", "start"],
                           G: ["start", "board:30", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "safe:5", "start", "start"],
                           G: ["start", "board:30", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],}],
                         result)

    def test_game_compute_states_7(self):
        game = Game()
        result = game.computePossibleGameStates(7, Y)
        self.assertEqual([], result)

        threeActivePawns ={Y: ["board:4", "board:59", "safe:2", "start"],
                           G: ["start", "board:30", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],}
        game.setPawns(threeActivePawns)
        result = game.computePossibleGameStates(7, Y) 
        expectedMutations = [
                          # No split cases
                          {Y: ["board:11", "board:59", "safe:2", "start"],}, # A7
                          {Y: ["board:4", "safe:4", "safe:2", "start"],},    # B7
                          {Y: ["board:4", "board:59", "home", "start"],},    # C7

                          # Split between AxB
                          {Y: ["board:5", "safe:3", "safe:2", "start"],},    # A1,B6
                          # Invalid move                                     # A2,B5
                          {Y: ["board:7", "safe:1", "safe:2", "start"],},    # A3,B4
                          {Y: ["board:8", "board:2", "safe:2", "start"],},   # A4,B3
                          {Y: ["board:9", "board:1", "safe:2", "start"],},   # A5,B2
                          {Y: ["board:10", "board:0", "safe:2", "start"],},  # A6,B1
                          

                          # Split between AxC
                          {Y: ["board:5", "board:59", "home", "start"],},    # A1,C6
                          {Y: ["board:6", "board:59", "home", "start"],},    # A2,C5
                          {Y: ["board:7", "board:59", "home", "start"],},    # A3,C4
                          {Y: ["board:8", "board:59", "safe:5", "start"],},  # A4,C3
                          {Y: ["board:9", "board:59", "safe:4", "start"],},  # A5,C2
                          {Y: ["board:10", "board:59", "safe:3", "start"],}, # A6,C1
                          
                          # Split between BxC
                          {Y: ["board:4", "board:0", "home", "start"],},     # B1,C6
                          {Y: ["board:4", "board:1", "home", "start"],},     # B2,C5
                          {Y: ["board:4", "board:2", "home", "start"],},     # B3,C4
                          {Y: ["board:4", "safe:1", "safe:5", "start"],},    # B4,C3
                          {Y: ["board:4", "safe:2", "safe:4", "start"],},    # B5,C2
                          # Invalid move                                     # B6,C1
                          ]
        for item in expectedMutations:
            item.update({G:threeActivePawns[G],R:threeActivePawns[R],B:threeActivePawns[B]})

        self.assertEqual(sorted(expectedMutations),
                         sorted(result))

    def test_game_compute_states_4(self):
        game = Game()
        result = game.computePossibleGameStates(4, Y)
        self.assertEqual([], result)

        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates(4, G)
        self.assertEqual([{Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:26", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:30", "board:14", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],}], 
                         result)

    def test_game_compute_states_10(self):
        game = Game()
        result = game.computePossibleGameStates(10, Y)
        self.assertEqual([], result)

        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates(10, G)
        self.assertEqual([{Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:29", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:30", "board:17", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:40", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:30", "home", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          ], 
                         result)

    def test_game_compute_states_11(self):
        game = Game()
        result = game.computePossibleGameStates(11, Y)
        self.assertEqual([], result)

        game.setPawns(SAMPLE_PAWN_SETUP)
        result = game.computePossibleGameStates(11, G)
        self.assertEqual([{Y: ["board:30", "board:59", "start", "start"],
                           G: ["start", "board:4", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:30", "start", "start"],
                           G: ["start", "board:59", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:13", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:30"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:41", "safe:1", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},
                          {Y: ["board:4", "board:59", "start", "start"],
                           G: ["start", "board:30", "home", "start"],
                           R: ["start", "start", "home", "start"],
                           B: ["start", "safe:1", "start", "board:13"],},], 
                         result)

def keepKey(key, data):
    return {k: v for k, v in data.items() if k == key}

def main():
    unittest.main()

if __name__ == "__main__":
    main()